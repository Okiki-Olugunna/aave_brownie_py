What this project does:

1. Swaps ETH for WETH
2. Deposits ETH into Aave
3. Borrows an asset with the ETH collateral 
4. Repays everything back

Testing:
Integration tests: Kovan 
Unit tests: Mainnet-fork 


All the concepts here allows you to work with other contracts on different DEXs as well, such as Paraswap & Uniswap.


Could improve on this later by:
    - Selling the borrowed asset (Short selling) 
    - Redoing it for Aave V3, as this is for V2 
