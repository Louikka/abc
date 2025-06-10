
program fib

    use iso_fortran_env

    implicit none



    integer :: i, seq_length
    integer(kind = int64) :: x
    integer(kind = int64), allocatable :: arr(:)

    write(*, '(A)', advance='no') "Enter the length of Fibonacci sequence : "
    read(*,*) seq_length

    allocate(arr(seq_length))

    arr(1) = 0
    write(*, '(" ", I0)') arr(1)

    arr(2) = 1
    write(*, '(" ", I0)') arr(2)

    do i = 3, seq_length
        arr(i) = arr(i - 1) + arr(i - 2)

        if (arr(i) < 0) then
            write(*, '(A, I0, A)') "Next number is too big (largest possible number (int64) is ", huge(x), ")"
            write(*, '(A, I0)') "Length of the computed sequence : ", i - 1

            exit
        end if

        write(*, '(" ", I0)') arr(i)
    end do

end program fib
