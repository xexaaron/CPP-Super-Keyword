#include "../src/example/exampleGrandChild.hpp"

class exampleGreatGrandChild final : public exampleGrandChild {
public:
    exampleGreatGrandChild() = default;
    ~exampleGreatGrandChild() = default;
    void TestExample() override;
private:
protected:
};