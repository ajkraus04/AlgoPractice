/*
 You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

 You can either start from the step with index 0, or the step with index 1.

 Return the minimum cost to reach the top of the floor. 

 Ex:
    Cost = [10,15,20]
    Output = 15
 */



var minCostClimbingStairs = function(cost) {
    dp = new Array(cost.length)
    for (let i=0;i<cost.length;i++){
        if (i<=1){
            dp[i] = cost[i];
        } else{
            dp[i] = cost[i] + Math.min(dp[i-1], dp[i-2]);
        }
    }
    return Math.min(dp[dp.length-1], dp[dp.length-2])
};
