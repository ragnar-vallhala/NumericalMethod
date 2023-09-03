#include<iostream>
#include <vector>
#define uint unsigned int


struct dim{
    int a;
    int b;
    dim() = default;
    dim(int a,int b){
        this->a = a;
        this->b = b;
    }
};



class Vector{

public:


    Vector(uint num, double* arr);
    ~Vector();
    void print();
    Vector add(Vector);
    Vector negate();
    

private:
    uint num;
    double* values;
};

class Matrix{
public:
    Matrix(dim,std::vector<Vector>);
    Matrix reduceToU();
private:
    dim shape;
    std::vector<Vector> mat;
};




int main(){
    double arr[]{1,2,3,4,5};
    Vector v(5,arr);
    
    v.negate().print();
}










Vector::Vector(uint num, double *arr)
{
    this->num = num;
    this->values  = arr;
}

Vector::~Vector()
{
    delete this->values;
}

void Vector::print()
{
    std::cout<<"[";
    for(int i{};i<this->num-1;i++){
        std::cout<<this->values[i]<<", ";
    }
    std::cout<<this->values[this->num-1]<<"]";
}

Vector Vector::add(Vector in)
{

    double *arr = new double[this->num];
    
    for(int i{};i<this->num;i++){
        arr[i]=this->values[i] + in.values[i];
    }

    return Vector(in.num,arr);
}

Vector Vector::negate()
{
     double *arr = new double[this->num];
    
    for(int i{};i<this->num;i++){
        arr[i]= - this->values[i];
    }

    return Vector(this->num,arr);
}

Matrix::Matrix(dim shape, std::vector<Vector> mat)
{
    this->shape = shape;
    this->mat = mat;
}

Matrix Matrix::reduceToU()
{
    for(int i{};i<this->shape.a;i++){
        for(int j{i-1};j>=0;j++){
            
        }
    }
    return *this;
}
