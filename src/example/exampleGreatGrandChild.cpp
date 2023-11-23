#include "../../include/exampleGreatGrandChild.h"

exampleGreatGrandChild::exampleGreatGrandChild() {
    
}
exampleGreatGrandChild::~exampleGreatGrandChild() = default;

void exampleGreatGrandChild::TestExample() {
    printf("Testing exampleParent : Original Class Name is : %s\n", GetClassName().c_str());
}
