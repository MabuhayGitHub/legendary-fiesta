import grade

def main():
    scorelist = grade.readList()
    scorelist = grade.sortList(scorelist)
    grade.showScore(scorelist)

if __name__ == "__main__":
    main()