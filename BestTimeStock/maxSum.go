// 該array長度為該數字，輸出一個數字，該數字所有子集合中總和的最大值
//    Ex.
//    輸入
//		[2,-1,4,-2,2]
//    輸出 6 ，因為子集合為[2,4]加總最大
package main

import "fmt"
import "math"

func getMaxSum(arr []float64) float64 {
	var maxSum, sum, nowMax float64 = 0, 0, 0
	for _, v := range arr {
		sum = v + nowMax
		nowMax = math.Max(nowMax, v)
		maxSum = math.Max(maxSum, sum)
		// fmt.Printf("nowMax:%v, sum:%v, maxSum:%v \n", nowMax, sum, maxSum)
	}
	return maxSum
}

func main() {
	var arr []float64 = []float64{2, -1, 4, -2, 2}
	fmt.Println(getMaxSum(arr))
}
