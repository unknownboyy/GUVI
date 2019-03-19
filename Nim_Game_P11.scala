import java.util._
object NimGame{
    def main(args: Array[String]): Unit = {
        var in = new Scanner(System.in)
        var n = in.nextInt
        var arr = new ArrayList[Int];
        var s = new HashSet[Int];
        for(i <- 0 until n){
            arr.add(in.nextInt)
            s.add(arr.get(i))

        }
        var x = 0
        var flag = false
        for(i<- 0 until n){
            x = x ^ arr.get(i)
            if (s.contains(x^i)) flag=true;
        }
        if (((x==0 || !s.contains(x)) && flag==true) || (flag==false && n>3))
        println("Alice")
        else
        println("Bob")
    }
}