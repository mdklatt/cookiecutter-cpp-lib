/// Header for the Greeting class.
///
#ifndef __HELLO_GREETING_HPP__
#define __HELLO_GREETING_HPP__


#include <string>


/// Generate a friendly greeting.
///
namespace Hello
{
    class Greeting
    {
    public:
        Greeting(const std::string& hello="Hello") : hello_(hello) {}
        std::string operator()(const std::string& name="World") const;
    
    private:
        const std::string hello_;
    };
}

#endif
