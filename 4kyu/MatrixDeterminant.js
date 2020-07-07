function determinant(m) {
if (m.length == 1)
      return m[0][0];
      function calculateDet(matrix) {
          if (matrix.length == 2)
          return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1];
          let res = 0, sign = 1;
          for (let i = 0; i < matrix[0].length; i++) {
              let aux = [];
              for (let j = 1; j < matrix.length; j++) {
                  aux.push([]);
                  for (let k = 0; k < matrix[0].length; k++) {
                      if (k != i) aux[j-1].push(matrix[j][k]);
                    }
                }
                res += matrix[0][i] * sign * calculateDet(aux.slice()); //like high school, remember your Math test
                sign *= -1;
            }
            return res;
        }
        return calculateDet(m);
};
