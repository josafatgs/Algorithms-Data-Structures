public class Recursion {

    //Implementacion con un String
    static void printReverse( int indice, String str) {
        if (str == null || indice >= str.length()){
            return ;
        }

        printReverse(indice + 1, str);
        System.out.println(str.charAt(indice));
    }

    //Implementacion con un Array
    static void printReverse(int indice, char [] str) {
        if (str == null || indice >= str.length){
            return ;
        }

        printReverse(indice + 1, str);
        System.out.println(str[indice]);
    }

    //Two Pointer Method this is not recursive method
    static void reverseString(char[] s) {

        if (s == null) {
            return;
        }
        
        int last = s.length - 1;
        int first = 0;
        
        while (first < last) {

            char temp = s[first];
            s[first] = s[last];
            s[last] = temp;

            first++;
            last--;
        }

        System.out.println(s);
    }

    //Two Pointer Method recursive
    static char[] reverseString(char[] s, int first, int last) {
        if (s == null || first >= last) {
            return s;
        }

        char temp = s[first];
        s[first] = s[last];
        s[last] = temp;

        reverseString(s, ++first, --last);
        return s;
    }

    public static void main(String [] Args) {
        //printReverse(0, "Hello World");
        //printReverse(0, "hello world".toCharArray());
        //reverseString("hello world".toCharArray());
        System.out.println(reverseString("hello world".toCharArray(), 0, "hello world".length() - 1));
    }
}