/**
 * Interface for the sample library module.
 *
 * @file
 */
#ifndef {{ cookiecutter.lib_name|upper }}_MODULE_HPP
#define {{ cookiecutter.lib_name|upper }}_MODULE_HPP


namespace {{ cookiecutter.lib_name }} {
    /**
     * Sample class.
     */
    class SampleClass {
    public:
        /**
         * Construct a SampleClass object.
         *
         * @param num any integer value
         */
        SampleClass(int num=0) : num{num} {}

        /**
         * Add a number.
         *
         * @param x any integer value
         * @return the sum of num and x.
         */
        int add(int x) const;
        
    private:
        const int num;
    };

    /**
     * Sample function.
     *
     * @param x any integer value
     * @param y any integer value
     * @return the sum of x and y
     */
    int add(int x, int y);
}

#endif  // {{ cookiecutter.lib_name|upper }}_MODULE_HPP 
