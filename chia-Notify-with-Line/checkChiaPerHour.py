import chiaUtil

estimatedPlotSizeTiB,eachProfile,currentBlockFound,alertPlotSizeTib = chiaUtil.getInfo()
chiaUtil.lineShowWarning(estimatedPlotSizeTiB,alertPlotSizeTib)