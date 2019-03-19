import java.util._
object Factorial{
    def fact(n:Int):Int = {
        if(n<=1)
        n
        else
        n*fact(n-1)
    }
    def main(args: Array[String]): Unit = {
        var in = new Scanner(System.in)
        var n = in.nextInt
        println(fact(n))
    }
}