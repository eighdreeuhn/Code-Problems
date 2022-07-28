function solveIt(excel){
  
    const _isValidRowSum = r => {
      let rowSum = 0 
      for (let i = 0; i < excel.length - 1; i++) {
        rowSum += excel[r][i]
      }
      if (excel[r][excel[r].length - 1] !== rowSum) {
        console.log(rowSum, excel[r][excel[r].length - 1])
        return false
      } else {
        return true
      }
    }
    
    const _isValidColumnSum = c => {
      let columnSum = 0 
      for (let j = 0; j < excel.length - 1; j++) {
        columnSum += excel[j][c]
      }
      if (excel[j][excel.length - 1] !== columnSum) {
        return false
      } else {
        return true
      }
    }
    
    const _findOffender = r => {
      for (let j = 0; j < excel[r].length - 1; j++) {
        return 'hi'
      }
    }
    
    for (let row in excel) {
      if (!_isValidRowSum(row)[0]) {
        return _findOffender(row)
      }
    }
  }