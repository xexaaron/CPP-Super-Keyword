#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <typeinfo>


class exampleParent {
public:
    // If you want to ignore the intellisense error when calling Super::func() add this code to your parent class.
    using Super = exampleParent; // this definition will be ignored as the keyword is replaced.
    // let me know if there is a better way to handle the intellisense errors.
    exampleParent();
    ~exampleParent();
private:
protected:
    virtual void TestExample();
    std::string GetClassName();  
};