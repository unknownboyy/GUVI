import java.util._
import scala.collection.JavaConversions._
object CommonDivisors{
    def gcd(a:Int,b:Int):Int = {
        if(b==0 || a%b==0)
        b
        else
        gcd(b,a%b)
    }
    def main(args: Array[String]): Unit = {
        var in = new Scanner(System.in);
        var t = in.nextInt
        for(a0 <- 0 until t){
            var a = in.nextInt
            var b = in.nextInt
            var c = gcd(a,b)
            var  count = 2
            for(i <- 2 to Math.sqrt(c).toInt){
                if(c%i==0)
                count += 2
            }
            if(Math.ceil(Math.sqrt(c))==Math.floor(Math.sqrt(c))){
                count-=1;
            }
            println(count)
        }
    }
}