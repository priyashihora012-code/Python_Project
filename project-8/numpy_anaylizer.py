import numpy as np

class DataAnalytics:

    def __init__(self, data=None):
        self.__array = (
            np.array(data, dtype=int)
            if data is not None
            else np.empty((0,), dtype=int)
        )

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, new_data):
        self.__array = np.array(new_data, dtype=int)

    def _check_shape(self, other_arr):
        if self.__array.shape != other_arr.shape:
            raise ValueError("Arrays must have identical dimensions!")

    @classmethod
    def from_string(cls, string_data, shape):
        flat = np.fromstring(string_data, sep=" ", dtype=int)
        return cls(flat.reshape(shape))

    @staticmethod
    def parse_slice(slice_str):
        if not slice_str or ":" not in slice_str:
            return slice(None)
        try:
            parts = slice_str.split(":")
            start = int(parts[0]) if parts[0] else None
            end = int(parts[1]) if parts[1] else None
            return slice(start, end)
        except (ValueError, IndexError):
            return slice(None)

    def get_element(self, indices):
        return self.__array[indices]

    def get_slice(self, row_slice, col_slice=None, depth_slice=None):
        if self.__array.ndim == 1:
            return self.__array[row_slice]
        elif self.__array.ndim == 2:
            return self.__array[row_slice, col_slice]
        elif self.__array.ndim == 3:
            return self.__array[row_slice, col_slice, depth_slice]
        return self.__array


    def combine_vertical(self, other_arr):
        return np.vstack((self.__array, other_arr))

    def split_array(self, sections):
        return np.array_split(self.__array, sections)

    def elementwise_add(self, other_arr):
        self._check_shape(other_arr)
        return np.add(self.__array, other_arr)

    def elementwise_subtract(self, other_arr):
        self._check_shape(other_arr)
        return np.subtract(self.__array, other_arr)

    def elementwise_multiply(self, other_arr):
        self._check_shape(other_arr)
        return np.multiply(self.__array, other_arr)

    def elementwise_divide(self, other_arr):
        self._check_shape(other_arr)
        res = np.divide(self.__array, other_arr, out=np.zeros_like(self.__array, dtype=float), where=other_arr != 0)
        return res.astype(int)


    def search_value(self, value):
        return np.where(self.__array == value)

    def sort_array(self):
        return np.sort(self.__array, axis=-1)

    def filter_condition(self, operator, threshold):
        match operator:
            case ">":
                mask = self.__array > threshold
            case "<":
                mask = self.__array < threshold
            case "==":
                mask = self.__array == threshold
            case ">=":
                mask = self.__array >= threshold
            case "<=":
                mask = self.__array <= threshold
            case _:
                mask = np.ones_like(self.__array, dtype=bool)
        return self.__array[mask]

    
    def compute_median(self):
        return float(np.median(self.__array))

    def compute_sum(self):
        return int(np.sum(self.__array))

    def compute_mean(self):
        return int(np.mean(self.__array))

    def compute_std(self):
        return int(np.std(self.__array))

    def compute_variance(self):
        return int(np.var(self.__array))


def main():
    analyzer = DataAnalytics()
    print("Welcome to the NumPy Analyzer!")
    print("==================================")

    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                print("\nSelect the type of array to create:")
                print("1. 1D Array\n2. 2D Array\n3. 3D Array")
                type_choice = input("Enter your choice: ").strip()

                try:
                    match type_choice:
                        case "1":
                            size = int(input("Enter the size of the 1D Array: "))
                            elems = input(f"Enter {size} elements separated by space: ")
                            analyzer.array = np.fromstring(elems, sep=" ", dtype=int).reshape((size,))
                        case "2":
                            rows = int(input("Enter the number of rows: "))
                            cols = int(input("Enter the number of columns: "))
                            elems = input(f"Enter {rows * cols} elements separated by space: ")
                            analyzer.array = np.fromstring(elems, sep=" ", dtype=int).reshape((rows, cols))
                        case "3":
                            depth = int(input("Enter the depth (dim 0): "))
                            rows = int(input("Enter the number of rows (dim 1): "))
                            cols = int(input("Enter the number of columns (dim 2): "))
                            elems = input(f"Enter {depth * rows * cols} elements separated by space: ")
                            analyzer.array = np.fromstring(elems, sep=" ", dtype=int).reshape((depth, rows, cols))
                        case _:
                            print("Invalid array type selected.")
                            continue

                    print("\nArray created successfully:\n", analyzer.array)

                    print("\nChoose an operation:\n1. Indexing\n2. Slicing\n3. GO Back")
                    sub_choice = input("Enter your choice: ").strip()

                    match sub_choice:
                        case "1":
                            idx_str = input("Enter indices separated by space: ")
                            indices = tuple(map(int, idx_str.split()))
                            print("Element:", analyzer.get_element(indices))
                        case "2":
                            match analyzer.array.ndim:
                                case 1:
                                    r_slice = DataAnalytics.parse_slice(input("Enter range (start:end): "))
                                    print("\nSliced Array:\n", analyzer.get_slice(r_slice))
                                case 2:
                                    r_slice = DataAnalytics.parse_slice(input("Enter row range (start:end): "))
                                    c_slice = DataAnalytics.parse_slice(input("Enter column range (start:end): "))
                                    print("\nSliced Array:\n", analyzer.get_slice(r_slice, c_slice))
                                case 3:
                                    d_slice = DataAnalytics.parse_slice(input("Enter depth/table range (start:end): "))
                                    r_slice = DataAnalytics.parse_slice(input("Enter row range (start:end): "))
                                    c_slice = DataAnalytics.parse_slice(input("Enter column range (start:end): "))
                                    print("\nSliced Array:\n", analyzer.get_slice(d_slice, r_slice, c_slice))
                        case _:
                            continue

                except Exception as e:
                    print(f"Error handling array: {e}")

            case "2":
                if analyzer.array.size == 0:
                    print("Please create an array first (Option 1).")
                    continue

                print("\nChoose a mathematical operation:")
                print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
                op_choice = input("Enter your choice: ").strip()

                if op_choice not in ["1", "2", "3", "4"]:
                    print("Invalid operation selection.")
                    continue

                try:
                    elems = input(
                        f"Enter the same-size array elements ({analyzer.array.size} elements separated by space):\n"
                    )
                    second_arr = np.fromstring(
                        elems, sep=" ", dtype=int
                    ).reshape(analyzer.array.shape)
                    print("\nOriginal Array:\n", analyzer.array)
                    print("Second Array:\n", second_arr)

                    match op_choice:
                        case "1":
                            print(
                                "\nResult of Addition:\n",
                                analyzer.elementwise_add(second_arr),
                            )
                        case "2":
                            print(
                                "\nResult of Subtraction:\n",
                                analyzer.elementwise_subtract(second_arr),
                            )
                        case "3":
                            print(
                                "\nResult of Multiplication:\n",
                                analyzer.elementwise_multiply(second_arr),
                            )
                        case "4":
                            print(
                                "\nResult of Division:\n",
                                analyzer.elementwise_divide(second_arr),
                            )
                except Exception as e:
                    print(f"Math operation failed: {e}")

            case "3":
                if analyzer.array.size == 0:
                    print("Please create an array first (Option 1).")
                    continue

                print("\nChoose an option:\n1. Combine Arrays\n2. Split Array")
                comb_choice = input("Enter your choice: ").strip()

                try:
                    match comb_choice:
                        case "1":
                            elems = input(
                                f"Enter elements of another array to combine ({analyzer.array.size} elements separated by space):\n"
                            )
                            second_arr = np.fromstring(
                                elems, sep=" ", dtype=int
                            ).reshape(analyzer.array.shape)
                            print("\nOriginal Array:\n", analyzer.array)
                            print("Second Array:\n", second_arr)
                            print(
                                "\nCombined Array (Vertical Stack):\n",
                                analyzer.combine_vertical(second_arr),
                            )
                        case "2":
                            sec = int(
                                input("Enter number of sections to split into: ")
                            )
                            for i, part in enumerate(
                                analyzer.split_array(sec)
                            ):
                                print(f"Split {i+1}:\n", part)
                        case _:
                            print("Invalid choice.")
                except Exception as e:
                    print(f"Operation failed: {e}")

            case "4":
                if analyzer.array.size == 0:
                    print("Please create an array first (Option 1).")
                    continue

                try:
                    print("\nChoose an option:")
                    print("1. Search a value")
                    print("2. Sort the array")
                    print("3. Filter values")

                    search_choice = input("Enter your choice: ").strip()

                    match search_choice:

                        case "1":
                            value = int(input("Enter value to search: "))

                            pos = analyzer.search_value(value)

                            print("\nOriginal Array:")
                            print(analyzer.array)

                            if len(pos[0]) == 0:
                                print("\nValue not found.")
                            else:
                                print("\nValue found at:")
                                for i in range(len(pos[0])):
                                    if analyzer.array.ndim == 1:
                                        print(pos[0][i])
                                    else:
                                        print(f"({pos[0][i]}, {pos[1][i]})")

                        case "2":

                            print("\nOriginal Array:")
                            print(analyzer.array)

                            print("\nSorted Array:")
                            print(analyzer.sort_array())

                            print("(Sorting applied row-wise.)")

                        case "3":

                            op = input("Enter condition (>, <, >=, <=, ==): ")

                            value = int(input("Enter value: "))

                            print("\nOriginal Array:")
                            print(analyzer.array)

                            print("\nFiltered Array:")
                            print(analyzer.filter_condition(op, value))

                        case _:
                            print("Invalid choice.")
                except Exception as e:
                    print(f"Operation failed: {e}")


            case "5":

                if analyzer.array.size == 0:
                    print("Please create an array first (Option 1).")
                    continue

                try:
                    print("\nChoose an aggregate/statistical operation:")
                    print("1. Sum")
                    print("2. Mean")
                    print("3. Median")
                    print("4. Standard Deviation")
                    print("5. Variance")
    

                    stat_choice = input("Enter your choice: ").strip()

                    print("\nOriginal Array:")
                    print(analyzer.array)

                    match stat_choice:

                        case "1":
                            print("\nSum of Array:", analyzer.compute_sum())
  
                        case "2":
                            print("\nMean of Array:", analyzer.compute_mean())

                        case "3":
                            print("\nMedian of Array:", analyzer.compute_median())

                        case "4":
                            print("\nStandard Deviation:", analyzer.compute_std())

                        case "5":
                            print("\nVariance:", analyzer.compute_variance())

                        case _:
                            print("Invalid choice.")
                            
                except Exception as e:
                    print(f"Operation failed: {e}")
                        

            case "6":
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break             

            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()