class MaxPooling:
    def __init__(self, step: tuple = (2, 2), size: tuple = (2, 2)) -> None:
        self.step = step
        self.size = size

    def validateMatrix(self, matrix: list) -> None:
        rowLength = len(matrix[0])
        if all(len(row) == rowLength for row in matrix):
            if all(type(i) in (int, float) for row in matrix for i in row):
                return
        raise ValueError("Неверный формат для первого параметра matrix.")

    def __call__(self, matrix: list) -> list:
        self.validateMatrix(matrix)

        rangeI = range(self.size[1], len(matrix) + 1, self.step[1])
        rangeJ = range(self.size[0], len(matrix[0]) + 1, self.step[0])

        return [[max(matrix[y][x]
                     for y in range(i - self.size[1], i)
                     for x in range(j - self.size[0], j)
                     ) for j in rangeJ]
                for i in rangeI]