# libの構成
add_library(hlib STATIC hello.cpp hello.h)

# インクルードディレクトリの登録（hlibに依存するターゲットの生成時に参照される）
target_include_directories(hlib PUBLIC ${PROJECT_SOURCE_DIR}/hello)

