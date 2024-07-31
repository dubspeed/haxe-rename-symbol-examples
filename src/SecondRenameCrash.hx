package src;

import haxe.macro.Context;
import haxe.macro.Expr;

using haxe.macro.Tools;

class TestCrashMacro {
	static function combine(structure:Expr):Expr {
		if (structure.expr.match(EDisplay(_, DKMarked))) {
			return macro @:pos(Context.currentPos()) ($structure : {});
		}
        return Expr();
	}
}
