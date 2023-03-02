# HW4 Problem 2
# Note: Levermore step y-tilde_1/2 is wrong
# So I recalculated the entirety of step 1 as well
# Writing Runge Kutta python script because im lazy (and a cs major)


def rungekutta(ti = 0, yi = 1, h=0.2, s=3):
    #first we define the function we are trying to approximate
    def sol(x,y):
        return x**2 + y**2
    for i in range(1,s+1):
        #summoning the strength of 1000 suns to write this code
        print("Step " + str(i) + ":")
        t1half = ti + h/2
        t1half = round(t1half, 5)
        t1 = ti + h
        t1 = round(t1, 5)
        fz = sol(ti, yi)
        fz = round(fz, 5)
        print("f" + str(i-1) + " = f(" + str(ti)+ "," + str(yi) + ")", "=", fz)
        ytmid = yi + 1/2*h*fz
        ytmid = round(ytmid, 5)
        print("y-tilde_" + str(2*(i-1)+1) + "/2 =", yi, "+", "1/2 *", h, "*", fz, "=", ytmid)
        ftmid = sol(t1half, ytmid)
        ftmid = round(ftmid, 5)
        print("f-tilde_" + str(2*(i-1)+1) + "/2 = f(" +  str(t1half) + "," + str(ytmid) + ")", "=", ftmid)
        ymid = yi + 1/2*h*ftmid
        ymid = round(ymid, 5)
        print("y_" + str(2*(i-1)+1) + "/2 =", yi, "+" , "1/2 *", h, "*", ftmid, "=", ytmid, "=", ymid)
        fmid = sol(t1half, ymid)
        fmid = round(fmid, 5)
        print("f_" + str(2*(i-1)+1) + "/2 = f(" + str(t1half) + "," + str(ymid) + ")", "=", ftmid, "=", fmid)
        yt1 = yi + h*fmid
        yt1 = round(yt1, 5)
        print("y-tilde_" + str(i) + " =", yi, "+", h , "*", fmid, "=", yt1)
        ft1 = sol(t1, yt1)
        ft1 = round(ft1, 5)
        print("f_" + str(i) + " = f(" + str(t1) + "," + str(yt1) + ")", "=", ft1)
        out = yi + 1/6*h*(fz + 2*ftmid + 2*fmid + ft1)
        out = round(out, 5)
        print("final value for step " + str(i) + ": y" + str(i) + " = " + str(out))
        ti = t1
        yi = out


rungekutta()
