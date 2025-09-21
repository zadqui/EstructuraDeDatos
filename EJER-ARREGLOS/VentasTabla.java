public class VentasTabla {
    static String[] meses = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};
    static String[] departamentos = {"Ropa", "Deportes", "Juguetería"};

    
    static int[][] ventas = new int[12][3];

    
    public static void insertarVenta(String mes, String departamento, int valor) {
        int i = obtenerIndiceMes(mes);
        int j = obtenerIndiceDepartamento(departamento);
        ventas[i][j] = valor;
    }

    
    public static int buscarVenta(String mes, String departamento) {
        int i = obtenerIndiceMes(mes);
        int j = obtenerIndiceDepartamento(departamento);
        return ventas[i][j];
    }

   
    public static void eliminarVenta(String mes, String departamento) {
        int i = obtenerIndiceMes(mes);
        int j = obtenerIndiceDepartamento(departamento);
        ventas[i][j] = 0;
    }

    public static void mostrarTabla() {
        System.out.printf("%-12s %-10s %-10s %-12s%n", "Mes", "Ropa", "Deportes", "Juguetería");
        System.out.println("---------------------------------------------------");
        for (int i = 0; i < meses.length; i++) {
            System.out.printf("%-12s %-10d %-10d %-12d%n", 
                meses[i], ventas[i][0], ventas[i][1], ventas[i][2]);
        }
    }

    public static void totalPorDepartamento() {
        System.out.println("\nTotales por departamento:");
        for (int j = 0; j < departamentos.length; j++) {
            int suma = 0;
            for (int i = 0; i < ventas.length; i++) {
                suma += ventas[i][j];
            }
            System.out.println(departamentos[j] + ": " + suma);
        }
    }

 
    private static int obtenerIndiceMes(String mes) {
        for (int i = 0; i < meses.length; i++) {
            if (meses[i].equalsIgnoreCase(mes)) return i;
        }
        return -1; 
    }

    private static int obtenerIndiceDepartamento(String dep) {
        for (int i = 0; i < departamentos.length; i++) {
            if (departamentos[i].equalsIgnoreCase(dep)) return i;
        }
        return -1; 
    }

 
    public static void main(String[] args) {

        insertarVenta("Enero", "Ropa", 1500);
        insertarVenta("Febrero", "Deportes", 2200);
        insertarVenta("Marzo", "Juguetería", 1800);

        mostrarTabla();

      
        System.out.println("\nBuscar Febrero-Deportes: " + buscarVenta("Febrero", "Deportes"));

        eliminarVenta("Enero", "Ropa");
        System.out.println("Después de eliminar Enero-Ropa: " + buscarVenta("Enero", "Ropa"));

        totalPorDepartamento();
    }
}
