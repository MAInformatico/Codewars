public class Kata {
	public static int[][] matrixAddition(int[][] a, int[][] b) {
	int[][] resultado = new int[a.length][a[0].length];    
    for (int fila=0; fila<a.length; fila++){        
        for (int col=0; col<a[fila].length; col++){
            resultado[fila][col] = a[fila][col] + b[fila][col];
        }
    }
  return resultado;
	}
}
