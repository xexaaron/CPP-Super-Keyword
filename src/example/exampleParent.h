#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <typeinfo>

class exampleParent {
public:
    exampleParent();
    ~exampleParent();
private:
protected:
    using Super = exampleParent;
    virtual void TestExample();
    std::string GetClassName();  
};