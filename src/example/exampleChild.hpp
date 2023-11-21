#include "exampleParent.h"


class exampleChild : public exampleParent {
public:


    exampleChild() = default;
    ~exampleChild() = default;
    void TestExample() override {
        Super::TestExample();
        printf("Testing exampleChild : Original Class Name is : %s\n", GetClassName().c_str());
    }
private:
protected:
};