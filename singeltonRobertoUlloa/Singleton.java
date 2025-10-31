package refactoring_guru.singleton.example.non_thread_safe;

public class Singleton {
    private static Singleton instancia;
    public String valor;

    private Singleton(String valor) {
        this.valor = valor;
    }

    public static Singleton obtenerInstancia(String valor) {
        if (instancia == null) {
            instancia = new Singleton(valor);
        }
        return instancia;
    }
}