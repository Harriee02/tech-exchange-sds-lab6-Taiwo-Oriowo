answerDict = {
"New York" : "albany",
"California" : "sacramento",
"Alabama" : "montgomery",
"Ohio": "columbus",
"Utah": "salt lake city"
}

def checkAnswer(answer):
    resultsDict = {}
    for k,v in answer.items():
        if answerDict[k] == v:
            resultsDict[k] = True
        else:
            resultsDict[k] = False
    return resultsDict


#print(checkAnswer({"New York": "albany","Utah": "salt lake city"}))