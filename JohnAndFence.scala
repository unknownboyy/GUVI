import java.util._
import scala.collection.JavaConversions._
object JohnAndFence{
    def min(a:Int,b:Int):Int = {
        if(a<b)
        a
        else
        b
    }
    def main(args: Array[String]): Unit = {
        var in = new Scanner(System.in)
        var n = in.nextInt
        var arr : Array[Int];
        for(i <- 0 until n){
            arr(i) = in.nextInt
        }
        var left : Array[Int];
        var right :  Array[Int];
        left(0)=arr(0)
        right(n-1)=arr(n-1)

        for(i <- 1 until n){
            left(i)=min(left(i-1),arr(i))
        }
        for(i <- (0 until n-2).reverse){
            right(i)=min(right(i+1),arr(i))
        }
        var maxx = 0;
        for(i <- 0 until n){
            
        }
    }
}