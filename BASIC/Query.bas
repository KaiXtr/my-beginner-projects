rem "First BASIC program made by KaiXtr"
rem "For MikeOS"

dim as integer n1, n2, ope
dim as string asw

cls

function opadd(n1 as integer, n2 as integer) as integer
    return n1+n2
end function

function opsub(n1 as integer, n2 as integer) as integer
    return n1-n2
end function

function opmul(n1 as integer, n2 as integer) as integer
    return n1*n2
end function

function opdiv(n1 as integer, n2 as integer) as integer
    return n1/n2
end function

do until asw="no"
    print "Entry the first number:"
    input "> ", n1
    print
    print "Entry the second number:"
    input "> ", n2
    cls
    print "What you want to do with "+str(n1)+" and "+str(n2)+"?"
    color 4,0
    print "1-Add"
    color 6,0
    print "2-Subtract"
    color 2,0
    print "3-Multiply"
    color 1,0
    print "4-Divide"
    color 7,0
    print
    ope=10
    do until ope<5
        input "> ", ope
        print
        if ope=1 then
            print "The result is "+str(opadd(n1,n2))
        elseif ope=2 then
            print "The result is "+str(opsub(n1,n2))
        elseif ope=3 then
            print "The result is "+str(opmul(n1,n2))
        elseif ope=4 then
            print "The result is "+str(opdiv(n1,n2))
        else
            print "Invalid Operation"
        end if
    loop
    print
    print "Keep Calculating?"
    input "> ", asw
    if asw="yes" then
        cls
    end if
loop
cls
print "Thanks for using my calculator!"
sleep
end