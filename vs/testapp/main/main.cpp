#include "hello.h"

#ifdef _WIN32
#define MES001 "windowsなメッセージ"
#else
#define MES001 "it is not windows message"
#endif

int main()
{
	std::cout << MES001 << std::endl;

	return hello();
}