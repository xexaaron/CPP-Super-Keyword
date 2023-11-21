#include "exampleParent.h"

exampleParent::exampleParent() {
    
}
exampleParent::~exampleParent() = default;

void exampleParent::TestExample() {
    printf("Testing exampleParent : Original Class Name is : %s\n", GetClassName().c_str());
}

std::string exampleParent::GetClassName() {
    const char* name = typeid(*this).name();
    std::string m_name = name;
    std::string toErase = "class";
    size_t pos = m_name.find(toErase);
    if (pos != std::string::npos) {
        m_name.erase(pos, toErase.length());
    }
    m_name.erase(std::remove_if(m_name.begin(), m_name.end(), ::isspace), m_name.end());
    return m_name;
}