package src;

class A {
    public function new(vo:{}) {}
}

class CrashInForLoop {
    final _vo = {posts:[]};

    inline final function updatePosts() {
        var posts = [for (vo in _vo.posts) (new A(vo)) ];
    }
}