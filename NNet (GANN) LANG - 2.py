import numpy as np
import math
import random

import json
import os, sys

import pickle

enw = """the
of
to
and
a
in
is
it
you
that
he
was
for
on
are
with
as
I
his
they
be
at
one
have
this
from
or
had
by
hot
word
but
what
some
we
can
out
other
were
all
there
when
up
use
your
how
said
an
each
she
which
do
their
time
if
will
way
about
many
then
them
write
would
like
so
these
her
long
make
thing
see
him
two
has
look
more
day
could
go
come
did
number
sound
no
most
people
my
over
know
water
than
call
first
who
may
down
side
been
now
find"""

cw = """
1	的	95.9	de		04-Sep-2009
2	一	94.3	yī		11-Jul-2009
3	是	93.0	shì		28-Jul-2009
4	不	91.8	bù		08-May-2009
5	了	90.7	le		30-Jun-2009
6	在	89.7	zài		16-Sep-2009
7	人	88.7	rén		29-Jun-2009
8	有	87.8	yǒu		23-Feb-2010
9	我	86.9	wǒ		21-May-2009
10	他	86.1	tā		25-May-2009
11	这	85.3	zhè		03-Aug-2009
12	个	84.7	gè		31-Jul-2009
13	们	84.1	men		29-May-2009
14	中	83.5	zhōng		02-Nov-2009
15	来	82.9	lái		05-Jun-2009
16	上	82.4	shàng		12-May-2009
17	大	81.8	dà		02-Sep-2009
18	为	81.3	wèi		03-Nov-2009
19	和	80.8	hé		04-Nov-2009
20	国	80.3	guó		09-Nov-2009
21	地	79.8	dì		20-Nov-2009
22	到	79.3	dào		27-Nov-2009
23	以	78.8	yǐ		09-Dec-2009
24	说	78.4	shuō		05-Nov-2009
25	时	77.9	shí		10-Nov-2009
26	要	77.5	yào		30-Oct-2009
27	就	77.1	jiù		18-Dec-2009
28	出	76.7	chū		18-Sep-2009
29	会	76.3	huì		11-Nov-2009
30	可	76.0	kě		12-Nov-2009
31	也	75.6	yě		03-Jun-2009
32	你	75.2	nǐ		22-May-2009
33	对	74.9	duì		13-Nov-2009
34	生	74.5	shēng		30-Jul-2009
35	能	74.2	néng		30-Nov-2009
36	而	73.8	ér		07-Jan-2010
37	子	73.5	zǐ		24-Feb-2010
38	那	73.2	nà		04-Aug-2009
39	得	72.8	dé		11-Dec-2009
40	于	72.5	yú		08-Feb-2010
41	着	72.2	zhe		01-Dec-2009
42	下	71.9	xià		13-May-2009
43	自	71.6	zì		26-Jan-2010
44	之	71.2	zhī		20-Jan-2010
45	年	70.9	nián		07-Sep-2009
46	过	70.6	guò		19-Nov-2009
47	发	70.3	fā		23-Nov-2009
48	后	70.0	hòu		19-Jun-2009
49	作	69.8	zuò		24-Jun-2009
50	里	69.5	lǐ		09-Feb-2010
51	用	69.2	yòng		25-Jan-2010
52	道	68.9	dào		18-Feb-2010
53	行	68.7	xíng		23-Oct-2009
54	所	68.4	suǒ		15-Feb-2010
55	然	68.1	rán		05-Feb-2010
56	家	67.9	jiā		14-Aug-2009
57	种	67.6	zhòng		11-Jan-2010
58	事	67.3	shì		01-Feb-2010
59	成	67.1	chéng		28-Jan-2010
60	方	66.8	fāng		24-Nov-2009
61	多	66.6	duō		17-Nov-2009
62	经	66.3	jīng		10-Feb-2010
63	么	66.1	me		23-Jul-2009
64	去	65.8	qù		12-Aug-2009
65	法	65.5	fǎ		10-Dec-2009
66	学	65.4	xué		29-Jul-2009
67	如	65.1	rú		12-Jan-2010
68	都	64.9	dōu		04-Jun-2009
69	同	64.7	tóng		16-Nov-2009
70	现	64.4	xiàn		04-Jan-2010
71	当	64.2	dāng		25-Feb-2010
72	没	64.0	méi		22-Feb-2010
73	动	63.8	dòng		07-Dec-2009
74	面	63.6	miàn		17-Dec-2009
75	起	63.3	qǐ		22-Jan-2010
76	看	63.1	kàn		20-Aug-2009
77	定	62.9	dìng		05-Jan-2010
78	天	62.7	tiān		17-Jun-2009
79	分	62.5	fēn		19-Jan-2010
80	还	62.3	hái		06-Jan-2010
81	进	62.0	jìn		17-Sep-2009
82	好	61.8	hǎo		04-May-2009
83	小	61.6	xiǎo		03-Sep-2009
84	部	61.4	bù		12-Feb-2010
85	其	61.2	qí		04-Dec-2009
86	些	61.0	xiē		03-Feb-2010
87	主	60.8	zhǔ		29-Jan-2010
88	样	60.6	yàng		08-Jan-2010
89	理	60.4	lǐ		27-Jan-2010
90	心	60.2	xīn		26-Nov-2009
91	她	60.0	tā		26-May-2009
92	本	59.8	běn		08-Dec-2009
93	前	59.6	qián		18-Jun-2009
94	开	59.4	kāi		25-Nov-2009
95	但	59.2	dàn		02-Dec-2009
96	因	59.0	yīn		15-Jan-2010
97	只	58.8	zhǐ		03-Dec-2009
98	从	58.6	cóng		06-Nov-2009
99	想	58.4	xiǎng		18-Aug-2009
100	实	58.2	shí		14-Dec-2009"""

cw = cw.split()
cw = [i for i in cw if (cw.index(i)-3)%5==0]
enw = enw.split()

NEURAL_NET_SHAPE = (156, 20, 2)

CHINESE = np.matrix([0.0, 1.0])
ENGLISH = np.matrix([1.0, 0.0])

weights = []

def convert(char):
    if char in 'īǐíì': return 'i'
    elif char in 'ǎàāá': return 'a'
    elif char in 'ěēéè': return 'e'
    elif char in 'òóōǒ': return 'o'
    elif char in 'ùǔúū': return 'u'
    else: return char

def word_to_vector(word):
    a = [(char,'abcdefghijklmnopqrstuvwxyz'.index(convert(word[char]).lower())) for char in range(len(word))]
    v = [0.0 for i in range(26) for c in range(6)]
    for pos in a:
        v[pos[0]*26+pos[1]] = 1.0
    return v

def get_language(word):
    loadDNA(best)
    a = calc( word_to_vector( word ) )
    print("English: {}%, Chinese: {}%".format(round(a.item(0,0)*100,1),round(a.item(0,1)*100,1)))

TRAINING = [( w, CHINESE ) for w in cw] + [( w, ENGLISH ) for w in enw]

#Neural Net
def sigma(val):
    return 1/(1+math.exp(-val))
  
def sigmoid( matrix ):
    m = matrix.copy()
    for x in range(m.shape[0]):
        for y in range(m.shape[1]):
          m.itemset(x,y,sigma(m.item(x,y)))
    return m
  
def calc( i ):
    l = i
    for w in weights:
        l = sigmoid( l * w )
    return l
  
def loadDNA( dna ):
    global weights
    weights = [
        np.matrix( [ [dna[20*i+k] for k in range(20)] for i in range(156) ] ),
        np.matrix( [ [dna[3119 + 2*i+k] for k in range(2)] for i in range(20) ] ),
        ]

#Genetic Algorithm
def generateDNA():
    return [random.random()*2-1 for i in range(3160)]
  
def mutateDNA( dna ):
    tDna = dna.copy()
    if random.randint(0,2):
        for b in range( random.randint(0,20) ):
            i = random.randint(0,3159)
            tDna[i] = tDna[i] + random.random()*50-25
    return tDna
  
def off(m1, m2):
    return abs(m1.item(0,0) - m2.item(0,0)) + abs(m1.item(0,1) - m2.item(0,1))

def evaluate( dna ):
    loadDNA( dna )
    return sum([off(calc(np.matrix(word_to_vector(t[0]))), t[1]) for t in TRAINING])
  
#GANN LOOP
generation = [generateDNA() for i in range(50)]
l = pickle.load( open('bestnet156.net','rb') )
generation = [l for i in range(50)]
for gen in range(50000):
    generation.sort(key=evaluate)
    generation = generation[:10]*5
    print("generation " + str(gen) + ": " + str(evaluate(generation[0])))
    best = generation[0]
    generation = [mutateDNA(i) for i in generation]
