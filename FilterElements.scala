import java.util._
object FilterElements{
    def main(args: Array[String]): Unit = {
        var in = new Scanner(System.in);
        var t = in.nextInt
        for(a0 <- 1 to t){
            var n = in.nextInt
            var k = in.nextInt
            var x = 0
            var map = new HashMap[Int,Int]();
            var arr = new ArrayList[Int]();
            var set = new HashSet[Int]();
            var set2 = new HashSet[Int]();
            
            for(i <- 0 until n){
                x = in.nextInt
                if(map.containsKey(x)){
                    map.put(x,map.get(x)+1)
                } else{
                    map.put(x,1);
                    arr.add(x);
                }
                if(map.get(x)>=k){
                        set.add(x);
                }
            }
            if(arr.size()>0 && set.size()>0){
                for(i <- 0 until arr.size()){
                    if(set.contains(arr.get(i)) && !set2.contains(arr.get(i))){
                        print(arr.get(i)+" ")
                        set2.add(arr.get(i))
                    }
                }
                println("")
            } else{
                println("-1")
            }
        }
    }
}