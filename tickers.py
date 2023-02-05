import pandas as pd

symbols = sorted(['ABMD','ATVI','ADBE','AMD','AGNC','AKAM','ALXN','ALGN',
'ALKS','ALNY','GOOG','AABA','AMZN','DOX','UHAL','AMOV','AAL','AMGN','ADI','ANGI',
'ANSS','AAPL','AMAT','ACGL','ARCC','ASML','AZPN','ATHN','TEAM','ADSK','ADP','BIDU',
'OZRK','BIIB','BMRN','TECH','BLKB','BUFF','BLUE','BOKF','BKNG','BHF','AVGO','CHRW','CA',
'CDNS','CZR','CG','CAVM','CBOE','CDK','CDW','CELG','CERN','CHTR','CHKP','CINF','CTAS',
'CSCO','CTXS','CME','CGNX','CTSH','COLM','CMCSA','CBSH','COMM','CPRT','CSGP','COST','CACC','CSX','CTRP',
'CY','XRAY','DXCM','FANG','DISCB','DISCA','DISCK','DISH','DLTR','DBX','DNKN','ETFC','EWBC','EBAY',
'SATS','ESLT','EA','EQIX','ERIE','EXEL','EXPE','EXPD','ESRX','FFIV','FB','FAST',
'FITB','FSLR','FISV','FLEX','FLIR','FTNT','GLPI','GRMN','GLIBA','GNTX','GILD','GT','LOPE',
'HAS','HDS','HSIC','HOLX','HBANO','HBAN','IAC','IEP','ICLR','ICUI','IDXX','INFO',
'ILMN','INCY','INTC','IBKR','INTU','ISRG','IONS','IPGP','JBHT','JKHY','JAZZ',
'JD','JBLU','KLAC','KHC','LRCX','LAMR','LECO','LFUS','LKQ','LOGI','LOGM','LPLA',
'LULU','MSG','MKTX','MAR','MRVL','MTCH','MXIM','MELI','MEOH','MCHP','MU','MSCC',
'MSFT','MIDD','MKSI','MOMO','MDLZ','MNST','MYL','NDAQ','NATI','NKTR','NTAP','NTES',
'NFLX','NBIX','NWS','NWSA','NDSN','NTRS','NCLH','NTNX','NVDA','NXPI','ODFL','ON',
'OTEX','ORLY','PCAR','PACW','PAYX','PYPL','PBCT','PEP','PPC','PNFP','POOL','QQQ',
'PRAH','PFG','PFPT','PTC','QGEN','QRVO','QCOM','REGN','ROST','RGLD','RYAAY','SABR',
'SAGE','SBAC','STX','SGEN','SEIC','SHPG','SBNY','SINA','SIRI','SWKS','SPLK','SSNC',
'SBUX','STLD','SRCL','SIVB','SYMC','SNPS','TROW','TTWO','AMTD','TSLA','TXN','TMUS',
'TSCO','TRMB','TRIP','FOX','UBNT','ULTA','ULTI','VRSN','VRSK','VRTX','VIA','VIRT',
'VOD','WBA','WB','WDC','WLTW','WDAY','WYNN','XEL','XLNX','YNDX','ZBRA','ZG','ZION',
'VOO'
])

#df = pd.DataFrame(list(zip(symbols)),columns=['symbols'])
#print(nsdq.head(100))
#print(df["symbols"])