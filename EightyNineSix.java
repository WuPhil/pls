package learnstuff;

public class EightyNineSix {
	public static void main(String args[]) {
		int count = 0;
		System.out.println("[[[[[[[[[[[[[[[[[[[[[[89.5 SQUAD]]]]]]]]]]]]]]]]]]]]]]\n\n");
		for (int i = 1; i < 1000; i++) {
			int a = i;
			double b = .895*i;
			int c = (int) (b+0.5);
			double d = (double) c/a;
			if (d < .8955 && d >= .8945) {
				System.out.println(c + "/" + a);
				System.out.println(d);
				count++;
			}
		}
		System.out.println("\n\n\n\n" + count + "\n\n\n\n");
		
		//alright, the first possible tuple is 17/19
		//500 tuples in the first 1000 integers
		count = 0;
		
		System.out.println("\n\n[[[[[[[[[[[[[[[[[[[[[[[89.6 GANG]]]]]]]]]]]]]]]]]]]]]]]\n\n");
		for (int i = 1; i < 1000; i++) {
			int a = i;
			double b = .896*i;
			int c = (int) (b+0.5);
			double d = (double) c/a;
			if (d < .8965 && d >= .8955) {
				System.out.println(c + "/" + a);
				System.out.println(d);
				count++;
			}
		}
		
		System.out.println("\n\n\n\n" + count + "\n\n\n\n");
		//first tuple is 43/48
		//498 tuples in the first 1000 integers
	}
}
