
print("Enter total number of SAs taken (Max 4): ")
inputNumOfSA = float(input())
numOfSA = inputNumOfSA
if numOfSA == 1:
    print("Enter your raw score in SA1: ")
    inputRawSAScore = float(input())
    rawSA1Score = inputRawSAScore
    print("Enter number of items in SA1: ")  
    inputNumOfSA1Items = float(input())
    numOfSA1Items = inputNumOfSA1Items
    SA1 = rawSA1Score / numOfSA1Items

    print("Enter your raw FE score: ")
    inputRawFEScore = float(input())
    rawFEScore = inputRawFEScore
    print("Enter total FE items: ")
    inputNumOfFEItems = float(input())
    totalNumOfFEItems = inputNumOfFEItems

    totalSAGrade = SA1/numOfSA*100*0.75
    totalFEGrade = (rawFEScore/totalNumOfFEItems)*100*0.25
    finalGrade = totalSAGrade+totalFEGrade

    print("Grade Breakdown in 75/25")
    print("SA 75%: "+ str(totalSAGrade))
    print("FE 25%: "+ str(totalFEGrade))
    print("Final grade: "+ str(finalGrade))
elif numOfSA == 2:
    print("Enter your raw score in SA1: ")
    inputRawSAScore = float(input())
    rawSA1Score = inputRawSAScore
    print("Enter number of items in SA1: ")  
    inputNumOfSA1Items = float(input())
    numOfSA1Items = inputNumOfSA1Items
    SA1 = rawSA1Score / numOfSA1Items

    print("Enter your raw score in SA2: ")
    inputRawSAScore = float(input())
    rawSA2Score = inputRawSAScore
    print("Enter number of items in SA2: ")  
    inputNumOfSA2Items = float(input())
    numOfSA2Items = inputNumOfSA2Items
    SA2 = rawSA2Score / numOfSA2Items

    print("Enter your raw FE score: ")
    inputRawFEScore = float(input())
    rawFEScore = inputRawFEScore
    print("Enter total FE items: ")
    inputNumOfFEItems = float(input())
    totalNumOfFEItems = inputNumOfFEItems

    totalSAGrade = (((SA1 + SA2)/numOfSA)*100)*0.75
    totalFEGrade = ((rawFEScore/totalNumOfFEItems)*100)*0.25
    finalGrade = totalSAGrade+totalFEGrade

    print("Grade Breakdown in 75/25")
    print("SA 75%: "+ str(totalSAGrade))
    print("FE 25%: "+ str(totalFEGrade))
    print("Final grade: "+ str(finalGrade))
elif numOfSA == 3:
    print("Enter your raw score in SA1: ")
    inputRawSAScore = float(input())
    rawSA1Score = inputRawSAScore
    print("Enter number of items in SA1: ")  
    inputNumOfSA1Items = float(input())
    numOfSA1Items = inputNumOfSA1Items
    SA1 = rawSA1Score / numOfSA1Items

    print("Enter your raw score in SA2: ")
    inputRawSAScore = float(input())
    rawSA2Score = inputRawSAScore
    print("Enter number of items in SA2: ")  
    inputNumOfSA2Items = float(input())
    numOfSA2Items = inputNumOfSA2Items
    SA2 = rawSA2Score / numOfSA2Items

    print("Enter your raw score in SA3: ")
    inputRawSAScore = float(input())
    rawSA3Score = inputRawSAScore
    print("Enter number of items in SA3: ")  
    inputNumOfSA3Items = float(input())
    numOfSA3Items = inputNumOfSA3Items
    SA3 = rawSA3Score / numOfSA3Items

    print("Enter your raw FE score: ")
    inputRawFEScore = float(input())
    rawFEScore = inputRawFEScore
    print("Enter total FE items: ")
    inputNumOfFEItems = float(input())
    totalNumOfFEItems = inputNumOfFEItems

    totalSAGrade = (((SA1 + SA2+ SA3)/numOfSA)*100)*0.75
    totalFEGrade = ((rawFEScore/totalNumOfFEItems)*100)*0.25
    finalGrade = totalSAGrade+totalFEGrade

    print("Grade Breakdown in 75/25")
    print("SA 75%: "+ str(totalSAGrade))
    print("FE 25%: "+ str(totalFEGrade))
    print("Final grade: "+ str(finalGrade))

elif numOfSA == 4:
    print("Enter your raw score in SA1: ")
    inputRawSAScore = float(input())
    rawSA1Score = inputRawSAScore
    print("Enter number of items in SA1: ")  
    inputNumOfSA1Items = float(input())
    numOfSA1Items = inputNumOfSA1Items
    SA1 = rawSA1Score / numOfSA1Items

    print("Enter your raw score in SA2: ")
    inputRawSAScore = float(input())
    rawSA2Score = inputRawSAScore
    print("Enter number of items in SA2: ")  
    inputNumOfSA2Items = float(input())
    numOfSA2Items = inputNumOfSA2Items
    SA2 = rawSA2Score / numOfSA2Items

    print("Enter your raw score in SA3: ")
    inputRawSAScore = float(input())
    rawSA3Score = inputRawSAScore
    print("Enter number of items in SA3: ")  
    inputNumOfSA3Items = float(input())
    numOfSA3Items = inputNumOfSA3Items
    SA3 = rawSA3Score / numOfSA3Items

    print("Enter your raw score in SA4: ")
    inputRawSAScore = float(input())
    rawSA4Score = inputRawSAScore
    print("Enter number of items in SA4: ")  
    inputNumOfSA4Items = float(input())
    numOfSA4Items = inputNumOfSA4Items
    SA4 = rawSA4Score / numOfSA4Items

    print("Enter your raw FE score: ")
    inputRawFEScore = float(input())
    rawFEScore = inputRawFEScore
    print("Enter total FE items: ")
    inputNumOfFEItems = float(input())
    totalNumOfFEItems = inputNumOfFEItems

    totalSAGrade = ((SA1 + SA2 + SA3 + SA4)/numOfSA)*100*0.75
    totalFEGrade = (rawFEScore/totalNumOfFEItems)*100*0.25
    finalGrade = totalSAGrade+totalFEGrade

    print("Grade Breakdown in 75/25")
    print("SA 75%: "+ str(totalSAGrade))
    print("FE 25%: "+ str(totalFEGrade))
    print("Final grade: "+ str(finalGrade))
else:
    print("Can't Calculate more than 4 SAs")
    
    










