from clinical_effort.models import CTEffort, Cycles, Visits, PersonnelTypes, Personnel, PersonnelField, PersonnelDefaults


# Add person
def add_person(proj_id, type_id, amount):

    # Retrieve project and cycle
    project = CTEffort.objects.get(id=proj_id)
    type = PersonnelTypes.objects.get(id=type_id)
    defaults = type.personneldefaults_set.all()

    # Add person
    new_person = Personnel(instance=project, type=type, name=type.name, amount=1)
    new_person.save()

    # Add default fields
    for default in defaults:
        new_field = PersonnelField(instance=new_person, text=default.text)
        new_field.save()

    return True

# Add default people
def add_default_people(proj_id):

    # Retrieve project and personnel types
    project = CTEffort.objects.get(id=proj_id)
    types = PersonnelTypes.objects.all()

    # Add people
    for type in types:
        add_person(proj_id, type.id, 1)

    return True