select logo, cat.Name Categoria, cast (ChargeTrans+ ComissionClient as DECIMAL(18,2)) comision  from [dbo].[TAE_Carriers] car
inner join TAE_Category cat
on car.CategoryId=cat.CategoryId
