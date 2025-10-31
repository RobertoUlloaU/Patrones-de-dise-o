package refactoring_guru.singleton.example.non_thread_safe;

// Clase de demostración para probar el patrón Singleton
public class DemoSingleThread {
    public static void main(String[] args) {
        // Mensaje inicial explicando el propósito del programa
        System.out.println("Si ves el mismo valor, entonces se reutilizó el singleton (¡bien!)" + "\n" +
                "Si ves valores diferentes, entonces se crearon 2 singletons (¡mal!)" + "\n\n" +
                "RESULTADO:" + "\n");

        // Obtiene la instancia única del Singleton con el valor "FOO"
        Singleton singleton = Singleton.obtenerInstancia("FOO");
        // Intenta obtener otra instancia del Singleton con el valor "BAR"
        Singleton otroSingleton = Singleton.obtenerInstancia("BAR");

        // Imprime los valores de ambas instancias
        System.out.println(singleton.valor); // Debería imprimir "FOO"
        System.out.println(otroSingleton.valor); // También debería imprimir "FOO"
    }
}