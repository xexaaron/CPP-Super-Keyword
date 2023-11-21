#include "exampleChild.hpp"


class exampleGrandChild : public exampleChild {
public:
    exampleGrandChild() = default;
    ~exampleGrandChild() = default;
    void TestExample() override {
        Super::TestExample();
        printf("Testing exampleGrandChild : Original Class Name is : %s\n", GetClassName().c_str());
    }
private:
protected:
};