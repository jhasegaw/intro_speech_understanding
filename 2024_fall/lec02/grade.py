import unittest, homework2

# TestSequence
class Test(unittest.TestCase):
    def test_a(self):
        a = "This is a python string"
        self.assertIs(type(homework2.a),type(a),"a should have type %s but it has type %s"%(type(a),type(homework2.a)))
        self.assertEqual(homework2.a,a,"a should equal %s but it equals %s"%(a,homework2.a))

    def test_b(self):
        b = 7 % 3
        self.assertIs(type(homework2.b),type(b),"b should have type %s but it has type %s"%(type(b),type(homework2.b)))
        self.assertEqual(homework2.b,b,"b should equal %s but it equals %s"%(b,homework2.b))

    def test_c(self):
        c = 55 * 234
        self.assertIs(type(homework2.c),type(c),"c should have type %s but it has type %s"%(type(c),type(homework2.c)))
        self.assertEqual(homework2.c,c,"c should equal %s but it equals %s"%(c,homework2.c))

    def test_d(self):
        name1 = "KCGI"
        name2 = "Kyoto"
        d = name1 + ' @ ' + name2
        self.assertIs(type(homework2.d),type(d),"d should have type %s but it has type %s"%(type(d),type(homework2.d)))
        self.assertEqual(homework2.d,d,"d should equal %s but it equals %s"%(d,homework2.d))

    def test_e(self):
        e = round(3.458, 2)
        self.assertIs(type(homework2.e),type(e),"e should have type %s but it has type %s"%(type(e),type(homework2.e)))
        self.assertEqual(homework2.e,e,"e should equal %s but it equals %s"%(e,homework2.e))

    def test_f(self):
        f = str(57)
        self.assertIs(type(homework2.f),type(f),"f should have type %s but it has type %s"%(type(f),type(homework2.f)))
        self.assertEqual(homework2.f,f,"f should equal %s but it equals %s"%(f,homework2.f))

    def test_g(self):
        g = (5==9)
        self.assertIs(type(homework2.g),type(g),"g should have type %s but it has type %s"%(type(g),type(homework2.g)))
        self.assertEqual(homework2.g,g,"g should equal %s but it equals %s"%(g,homework2.g))

    def test_h(self):
        h = str(-23.0)
        self.assertIs(type(homework2.h),type(h),"h should have type %s but it has type %s"%(type(h),type(homework2.h)))
        self.assertEqual(homework2.h,h,"h should equal %s but it equals %s"%(h,homework2.h))

    def test_i(self):
        i = float(False)
        self.assertIs(type(homework2.i),type(i),"i should have type %s but it has type %s"%(type(i),type(homework2.i)))
        self.assertEqual(homework2.i,i,"i should equal %s but it equals %s"%(i,homework2.i))

    def test_j(self):
        j = bool("Python")
        self.assertIs(type(homework2.j),type(j),"j should have type %s but it has type %s"%(type(j),type(homework2.j)))
        self.assertEqual(homework2.j,j,"j should equal %s but it equals %s"%(j,homework2.j))

    def test_k(self):
        k = "print2"+"_squ"
        self.assertIs(type(homework2.k),type(k),"k should have type %s but it has type %s"%(type(k),type(homework2.k)))
        self.assertEqual(homework2.k,k,"You said k==%s, but either you missed some valid names, or you included some names that are not valid"%(homework2.k))
        
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
