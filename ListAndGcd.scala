import java.util._
import scala.collection.JavaConversions._
object ListAndGcd{
    def min(a:Int,b:Int):Int = {
        if(a<b)
        a
        else
        b
    }
    def main(args: Array[String]): Unit = {
        var in = new Scanner(System.in)
        var t = in.nextInt
        in.nextLine
        var map = new HashMap[Int,Int]();
        var set = new HashSet[Int]();
        var line = in.nextLine().split(" ")
        for(i <- 0 until line.length){
            if(i%2==1){
                map.put(line(i-1).toInt,line(i).toInt)
                set.add(line(i-1).toInt)
            }
        }
        for(a0 <- 1 until t){
            line = in.nextLine.split(" ")
            var temp = new HashSet[Int]();
            for(i <- 0 until line.length){
                if(i%2==1){
                    if(map.containsKey(line(i-1).toInt))
                    map.put(line(i-1).toInt,min(map.get(line(i-1).toInt),line(i).toInt))
                    temp.add(line(i-1).toInt)
                }
            }
            set.retainAll(temp)
        }
        var tree = new TreeMap[Int,Int](map)
        for((key,value) <- tree){
            if(set.contains(key))  print(key+" "+value+" ")
        }
    }
}