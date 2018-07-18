{\rtf1\ansi\ansicpg950\cocoartf1561\cocoasubrtf400
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset136 PingFangTC-Regular;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 '''
\f1 \uc0\u23558 \'a4\'40\u20010 \'a5\'bf\'be\'e3\u25968 \'a4\'c0\'b8\'d1\u36136 \'a6\'5d\u25968 \'a1\'43\'a8\'d2\'a6\'70\'a1\'47\u36755 \'a4\'4a
\f0 90,
\f1 \'a5\'b4\'a6\'4c\'a5\'58
\f0 90=2*3*3*5'''\
def form_of_mult():\
    t = [1,2,3,4,5,6,7,8,9]\
    a = []\
    for i in range(0,len(t)):\
        for j in range(0,len(t)):\
            add = t[i]*t[j]\
            a = a + [add]\
        print(a)\
        if len(a) == 9:\
            a = []\
    return a\
\
\
def total_pure():\
    a = sorted(range(101,201))\
    \
    b = sorted(range(1,201))\
    c = []\
    for i in range(101,200):\
        for j in range(1,200):\
            \
            if a[i] % b[j] == 0 and a[i] > b[j]:\
                b = a[:i]\
            print(b)\
\
            \
def flower_num():\
    flower = []\
    for i in range(101,1000):\
        a = int(i/100)\
        b = int(i/10%10)\
        c = i%10\
        \
        if a**3 + b**3 + c**3 == i:\
            \
            flower = flower + [i]\
    print(flower)\
            \
        \
\
}