import java.util._
object Palindrome{
    def func(xn:Int):Int = {
        var copy = xn
        var num = 0
        var n = xn
        while (n > 0){
            num = num * 10 + n % 10
            n = n / 10
        }
        if(copy == num)
        1
        else
        0
    }
    def main(args: Array[String]): Unit = {
        var in = new Scanner(System.in)
        var n = in.nextInt        
        if (func(n)==1)
        println("Palindrome")
        else
        println("Not Palindrome")
    }
}