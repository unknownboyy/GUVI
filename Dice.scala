import java.util._
object Solution {
    def solve(m:Int,n:Int):Int = {
        var points = Array.ofDim[Int](m,n)
        var top = Array.ofDim[Int](m,n)
        var bottom = Array.ofDim[Int](m,n)
        var left = Array.ofDim[Int](m,n)
        var right = Array.ofDim[Int](m,n)
        var front = Array.ofDim[Int](m,n)
        var back = Array.ofDim[Int](m,n)
        for(i <- 0 until m){
            for(j <- 0 until n){
                if(i==0 && j==0){
                    top(i)(j)=1
                    front(i)(j)=2
                    left(i)(j)=3
                    right(i)(j)=4
                    bottom(i)(j)=6
                    back(i)(j)=5
                    points(i)(j)=1
                }
                else if(i==0){
                    top(i)(j)=left(i)(j-1)
                    bottom(i)(j)=right(i)(j-1)
                    left(i)(j)=bottom(i)(j-1)
                    right(i)(j)=top(i)(j-1)
                    front(i)(j)=front(i)(j-1)
                    back(i)(j)=back(i)(j-1)
                    points(i)(j)+=points(i)(j-1)+top(i)(j)
                }
                else if(j==0){
                    top(i)(j)=back(i-1)(j)
                    bottom(i)(j)=front(i-1)(j)
                    left(i)(j)=left(i-1)(j)
                    right(i)(j)=right(i-1)(j)
                    front(i)(j)=top(i-1)(j)
                    back(i)(j)=bottom(i-1)(j)
                    points(i)(j)+=points(i-1)(j)+top(i)(j)
                }
                else{
                    if(left(i)(j-1)>back(i-1)(j)){
                        top(i)(j)=left(i)(j-1)
                        bottom(i)(j)=right(i)(j-1)
                        left(i)(j)=bottom(i)(j-1)
                        right(i)(j)=top(i)(j-1)
                        front(i)(j)=front(i)(j-1)
                        back(i)(j)=back(i)(j-1)
                        points(i)(j)+=points(i)(j-1)+top(i)(j)
                    }
                    else{
                        top(i)(j)=back(i-1)(j)
                        bottom(i)(j)=front(i-1)(j)
                        left(i)(j)=left(i-1)(j)
                        right(i)(j)=right(i-1)(j)
                        front(i)(j)=top(i-1)(j)
                        back(i)(j)=bottom(i-1)(j)
                        points(i)(j)+=points(i-1)(j)+top(i)(j)
                    }
                }
            }
        }
        points(m-1)(n-1)
    }
    def main(args: Array[String]) {
        var in = new Scanner(System.in);
        var t = in.nextInt
        for(a0 <- 1 to t){
            var m=in.nextInt
            var n=in.nextInt
            if (m>n && m!=1 && n!=1) println(solve(n,m))
            else println(solve(m,n))
        }
    }
}