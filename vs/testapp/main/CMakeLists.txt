# 実行ファイルの作成
add_executable(main main.cpp)

# リンクするライブラリの指示
target_link_libraries(main hlib)