from model.model import Executor
from model import config

if __name__ == "__main__":         
        
    MSFT = Executor('MSFT',config.start_date,config.end_date)
    MSFT.summary_stats()
    MSFT.initial_plot('adj_close')
    MSFT.window_selection([11*365,5*365,2*365,180,90],'adj_close')
    MSFT.strategy_preparation('ADBE','adj_close',180, 90)
    MSFT.backtesting(100000,1000,'adj_close')
    MSFT.neural_enhancement('adj_close',0.5,0.2,'relu','adam','mse',50,32)
    MSFT.enhanced_strategy(100000,1000,'ADBE','adj_close',365, 180)