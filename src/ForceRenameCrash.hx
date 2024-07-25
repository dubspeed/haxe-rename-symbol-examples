package src;

abstract TestCrash(String) to String {
	public static inline function fail(data:Dynamic):TestCrash {
		return cast '${data.a}_${data.b}_${data.c}_${false}';
	}
}