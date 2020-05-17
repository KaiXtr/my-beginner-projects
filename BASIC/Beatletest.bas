dim as integer level, ans

CLS
COLOR 3,0
PRINT "Are you a Beatles fan?"
PRINT
PRINT "I Gonna make you some questions"
PRINT "Depending of your answers, your 'Beatles fan' level will be decided"
PRINT
SLEEP
CLS
PRINT "1)-What is the Name of the four Beatles?"
PRINT
PRINT "1-Paul\Yoko\Jimi\Jack"
PRINT "2-John\Paul\George\Ringo"
PRINT "3-George\John\Bob\Yoko"
PRINT "4-John\Paul\Bob\Martin"
PRINT
SLEEP
INPUT "> ", ans
PRINT
IF ans=2 THEN
	PRINT "You Are Right!"
	level+=1
ELSE
	PRINT "You Missed..."
END IF
PRINT "Next Question..."
SLEEP
CLS
PRINT "2)-What is the signature of most beatles musics?"
PRINT
PRINT "1-I'm the walrus"
PRINT "2-Bob Dylan\Marley"
PRINT "3-Lennon\Mccartey"
PRINT "4-John Lennon"
PRINT
SLEEP
INPUT "> ", ans
PRINT
IF ans=3 THEN
	PRINT "You Are Right!"
	level+=1
ELSE
	PRINT "You Missed..."
END IF
PRINT "Next Question..."
SLEEP
CLS
PRINT "3)-What is the name of the era where beatles exploded in the start of their carreir?"
PRINT
PRINT "1-Beatles golden era"
PRINT "2-A Hard Day's Night"
PRINT "3-British Invasion"
PRINT "4-Beatlemania"
PRINT
SLEEP
INPUT "> ", ans
PRINT
IF ans=4 THEN
	PRINT "You Are Right!"
	level+=1
ELSE
	PRINT "You Missed..."
END IF
PRINT "Next Question..."
SLEEP
CLS
PRINT "4)-The First album of the Beatles to use a citar?"
PRINT
PRINT "1-Beatles for Sale"
PRINT "2-Rubber Soul"
PRINT "3-Sgt. Pepper's Lonely Hearts Club Band"
PRINT "4-Revolover"
PRINT
SLEEP
INPUT "> ", ans
PRINT
IF ans=2 THEN
	PRINT "You Are Right!"
	level+=1
ELSE
	PRINT "You Missed..."
END IF
PRINT "Next Question..."
SLEEP
CLS
PRINT "5)-What is the studio where most beatles musics was produced?"
PRINT
PRINT "1-Sony"
PRINT "2-Abbey Road"
PRINT "3-Parlophone"
PRINT "4-EMI"
PRINT
SLEEP
INPUT "> ", ans
PRINT
IF ans=2 THEN
	PRINT "You Are Right!"
	level+=1
ELSE
	PRINT "You Missed..."
END IF
PRINT "Next Question..."
SLEEP
CLS
PRINT "6)-The First Music videos of all time?"
PRINT
PRINT "1-Something\Oh Darling!"
PRINT "2-Yellow Submarine\Eleanor Rigby"
PRINT "3-Paperback Writer\Rain"
PRINT "4-Help!\Yesterday"
PRINT
SLEEP
INPUT "> ", ans
PRINT
IF ans=3 THEN
	PRINT "You Are Right!"
	level+=1
ELSE
	PRINT "You Missed..."
END IF
PRINT "Next Question..."
SLEEP
CLS
PRINT "7)-For lots of beatlemaniacs, the people who destroyed the Beatles?"
PRINT
PRINT "1-Ravi Shankar"
PRINT "2-George Martin"
PRINT "3-Bob Dylan"
PRINT "4-Yoko Ono"
PRINT
SLEEP
INPUT "> ", ans
PRINT
IF ans=4 THEN
	PRINT "You Are Right!"
	level+=1
ELSE
	PRINT "You Missed..."
END IF
PRINT "Next Question..."
SLEEP
CLS
PRINT "8)-Place were the beatles started?"
PRINT
PRINT "1-Seattle"
PRINT "2-Liverpool"
PRINT "3-London"
PRINT "4-England"
PRINT
SLEEP
INPUT "> ", ans
PRINT
IF ans=2 THEN
	PRINT "You Are Right!"
	level+=1
ELSEIF ans=4 THEN
	PRINT "Yeah...quite right, I will pass that"
	level+=1
ELSE
	PRINT "You Missed..."
END IF
PRINT "Next Question..."
SLEEP
CLS
PRINT "9)-First Beatles movie?"
PRINT
PRINT "1-Help!"
PRINT "2-Yellow Submarine"
PRINT "3-A Hard Day's Night"
PRINT "4-Magical Mystery Tour"
PRINT
SLEEP
INPUT "> ", ans
PRINT
IF ans=3 THEN
	PRINT "You Are Right!"
	level+=1
ELSE
	PRINT "You Missed..."
END IF
PRINT "Next Question..."
SLEEP
CLS
PRINT "PAUL IS DEAD"
PRINT
PRINT "1-yes"
PRINT "2-no way!"
PRINT
SLEEP
INPUT "> ", ans
PRINT
IF ans=2 then
	PRINT "You Are Right!"
	level+=1
ELSE
	PRINT "You Missed..."
END IF
SLEEP
CLS
PRINT "Now let's see your results..."
SLEEP
PRINT
PRINT "You have "+STR(level)+" points"
IF level=0 THEN
	PRINT "Sorry, surely you are not a huge beatles fan"
ELSEIF level<4 THEN
	PRINT "Not bad at all, you know something about them"
ELSEIF level<7 THEN
	PRINT "Nice! Not a Beatlemaniac exactly but know lot of things!"
ELSEIF level<10 THEN
	PRINT "Wow! you are really a good Beatles fan"
ELSE
	PRINT "Congratulations! You are a True Beatlemaniac!"
END IF
PRINT
SLEEP
CLS
PRINT "Thanks for try my Beatles test! ^^"
SLEEP
END