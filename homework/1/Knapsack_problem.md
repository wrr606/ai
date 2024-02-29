
有 n 個物品，每個物品的價值為 v[i]，重量為 w[i]，背包能承受的重量為 x
定義一個陣列 dp，dp[i] 代表當背包容量為 i 時擁有的最大價值

## 01背包問題解
```cpp
for(int i=1;i<=n;i++){
    for(int j=x;j>=w[i];j--){
        dp[j]=max(dp[j],dp[j-w[i]]+v[i]);
    }
}
```

## 無限背包問題解
```cpp
for(int i=1;i<=W;i++){
    for(int j=1;j<=n;j++){
        if(i>=w[j])
            dp[i]=max(dp[i],dp[i-w[j]]+v[j]);
    }
}
```